module Foobar
    class HookedExcerpt < Jekyll::Excerpt
      def initialize(doc)
        super
        trigger_hooks(:post_init)
      end
  
      def output
        @output ||= trigger_hooks(:post_render, renderer.run)
      end
  
      def renderer
        @renderer ||= Jekyll::Renderer.new(
          doc.site, self, site.site_payload
        )
      end
  
      def trigger_hooks(hook_name, *args)
        Jekyll::Hooks.trigger :excerpts, hook_name, self, *args
      end
    end
  end
  
  Jekyll::Hooks.register :excerpts, :post_init do |excerpt|
    Jekyll.logger.debug "Initialized:",
                        "Hooked Excerpt for #{excerpt.doc.inspect}"
  end
  
  Jekyll::Hooks.register :excerpts, :post_render do |excerpt, output|
    return output unless excerpt.doc.type == :posts
    Foobar.transform(output)
  end